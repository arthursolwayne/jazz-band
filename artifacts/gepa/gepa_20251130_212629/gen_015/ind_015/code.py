
import pretty_midi
from pretty_midi import Note, Instrument

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.resolution = 480  # 480 ticks per quarter note

# Define key and tempo
key = 'D'
tempo = 160  # BPM

# Time signature is 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0, ticks=0)

# Add time signature
pm.time_signature_changes.append(time_signature)

# Set tempo
pm.tempo_changes.append(pretty_midi.TempoChange(tempo=tempo, time=0))

# Create instruments
bass_instrument = Instrument(program=33)  # Double Bass
piano_instrument = Instrument(program=0)  # Acoustic Piano
drums_instrument = Instrument(program=0)  # Drums
sax_instrument = Instrument(program=64)  # Tenor Saxophone

pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drums_instrument)
pm.instruments.append(sax_instrument)

# Define a function to convert beat time to ticks (based on resolution)
def beat_to_ticks(beats):
    return beats * pm.resolution * 60 / tempo

# Bar 1: Drums only — build tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0
bar1_end = beat_to_ticks(1)

# Kick on 1
drums_instrument.notes.append(Note(36, 64, bar1_start, bar1_start + beat_to_ticks(0.125)))

# Snare on 2
drums_instrument.notes.append(Note(38, 64, bar1_start + beat_to_ticks(0.25), bar1_start + beat_to_ticks(0.25) + beat_to_ticks(0.125)))

# Hihat on every eighth
for i in range(8):
    hihat_time = bar1_start + beat_to_ticks(i * 0.125)
    drums_instrument.notes.append(Note(42, 64, hihat_time, hihat_time + beat_to_ticks(0.0625)))

# Bar 2-4: Full band enters — sax melody, bass line, piano comp, drums

# Time for bar 2
bar2_start = bar1_end

# Saxophone melody — your motif: Start with a short phrase, leave it hanging, then resolve
# Notes in D: D, F#, A, B, C#, D
# Pattern: D (quarter) — rest (eighth) — F# (eighth) — A (eighth), then repeat with variation

# Bar 2: Start the motif
sax_note1 = Note(62, 80, bar2_start, bar2_start + beat_to_ticks(0.5))  # D4
sax_instrument.notes.append(sax_note1)

# Rest (eighth note)
# No note here

# F# (eighth)
sax_note2 = Note(64, 80, bar2_start + beat_to_ticks(0.5), bar2_start + beat_to_ticks(0.75))
sax_instrument.notes.append(sax_note2)

# A (eighth)
sax_note3 = Note(65, 80, bar2_start + beat_to_ticks(0.75), bar2_start + beat_to_ticks(1.0))
sax_instrument.notes.append(sax_note3)

# Bar 3: Continue motif with variation
bar3_start = bar2_start + beat_to_ticks(1)

# Rest (eighth)
# No note here

# B (eighth)
sax_note4 = Note(66, 80, bar3_start + beat_to_ticks(0.25), bar3_start + beat_to_ticks(0.5))
sax_instrument.notes.append(sax_note4)

# C# (eighth)
sax_note5 = Note(67, 80, bar3_start + beat_to_ticks(0.5), bar3_start + beat_to_ticks(0.75))
sax_instrument.notes.append(sax_note5)

# D (eighth)
sax_note6 = Note(62, 80, bar3_start + beat_to_ticks(0.75), bar3_start + beat_to_ticks(1.0))
sax_instrument.notes.append(sax_note6)

# Bar 4: Resolve the motif with a half note
bar4_start = bar3_start + beat_to_ticks(1)

# D (half note)
sax_note7 = Note(62, 80, bar4_start, bar4_start + beat_to_ticks(2.0))
sax_instrument.notes.append(sax_note7)

# Bass line: Chromatic walking line (D, E, F, G, A, B, C, D)
# Bar 2: D (quarter) -> E (eighth) -> F (eighth) -> G (eighth)
# Bar 3: A (quarter) -> B (eighth) -> C (eighth) -> D (eighth)
# Bar 4: D (half)

bass_notes = [
    Note(62, 64, bar2_start, bar2_start + beat_to_ticks(0.5)),  # D
    Note(63, 64, bar2_start + beat_to_ticks(0.5), bar2_start + beat_to_ticks(0.75)),  # E
    Note(64, 64, bar2_start + beat_to_ticks(0.75), bar2_start + beat_to_ticks(1.0)),  # F
    Note(65, 64, bar3_start, bar3_start + beat_to_ticks(0.5)),  # G
    Note(66, 64, bar3_start + beat_to_ticks(0.5), bar3_start + beat_to_ticks(0.75)),  # A
    Note(67, 64, bar3_start + beat_to_ticks(0.75), bar3_start + beat_to_ticks(1.0)),  # B
    Note(68, 64, bar4_start, bar4_start + beat_to_ticks(0.5)),  # C
    Note(69, 64, bar4_start + beat_to_ticks(0.5), bar4_start + beat_to_ticks(1.0)),  # D
]

for note in bass_notes:
    bass_instrument.notes.append(note)

# Piano: 7th chords on 2 and 4
# D7: D, F#, A, C
# Bar 2: on beat 2 (0.25), chord D7, held for 1 beat
piano_notes = [
    # Bar 2: D7 on beat 2
    Note(62, 80, bar2_start + beat_to_ticks(0.25), bar2_start + beat_to_ticks(0.25) + beat_to_ticks(0.5)),
    Note(64, 80, bar2_start + beat_to_ticks(0.25), bar2_start + beat_to_ticks(0.25) + beat_to_ticks(0.5)),
    Note(65, 80, bar2_start + beat_to_ticks(0.25), bar2_start + beat_to_ticks(0.25) + beat_to_ticks(0.5)),
    Note(67, 80, bar2_start + beat_to_ticks(0.25), bar2_start + beat_to_ticks(0.25) + beat_to_ticks(0.5)),

    # Bar 3: D7 on beat 2
    Note(62, 80, bar3_start + beat_to_ticks(0.25), bar3_start + beat_to_ticks(0.25) + beat_to_ticks(0.5)),
    Note(64, 80, bar3_start + beat_to_ticks(0.25), bar3_start + beat_to_ticks(0.25) + beat_to_ticks(0.5)),
    Note(65, 80, bar3_start + beat_to_ticks(0.25), bar3_start + beat_to_ticks(0.25) + beat_to_ticks(0.5)),
    Note(67, 80, bar3_start + beat_to_ticks(0.25), bar3_start + beat_to_ticks(0.25) + beat_to_ticks(0.5)),
]

for note in piano_notes:
    piano_instrument.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bars 2-4
for bar in range(2, 5):
    bar_start = beat_to_ticks(bar - 2) + bar2_start
    bar_end = bar_start + beat_to_ticks(1)

    # Kick on 1
    drums_instrument.notes.append(Note(36, 64, bar_start, bar_start + beat_to_ticks(0.125)))

    # Snare on 2
    drums_instrument.notes.append(Note(38, 64, bar_start + beat_to_ticks(0.25), bar_start + beat_to_ticks(0.25) + beat_to_ticks(0.125)))

    # Hihat on every eighth
    for i in range(8):
        hihat_time = bar_start + beat_to_ticks(i * 0.125)
        drums_instrument.notes.append(Note(42, 64, hihat_time, hihat_time + beat_to_ticks(0.0625)))

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file created: 'dante_intro.mid'")
