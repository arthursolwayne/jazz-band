
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI()

# Set tempo to 160 BPM
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.instruments = []

# Define the time in seconds per bar
BPM = 160
seconds_per_beat = 60.0 / BPM
seconds_per_bar = 4 * seconds_per_beat  # Each bar is 4 beats

# Create instruments for each player
# 1. Little Ray - Drums
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drum_instrument = Instrument(program=drum_program, is_drum=True, name='Drums')
midi.instruments.append(drum_instrument)

# 2. Marcus - Bass
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass_instrument = Instrument(program=bass_program, name='Bass')
midi.instruments.append(bass_instrument)

# 3. Diane - Piano
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_instrument = Instrument(program=piano_program, name='Piano')
midi.instruments.append(piano_instrument)

# 4. Dante - Tenor Sax
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax_instrument = Instrument(program=sax_program, name='Tenor Sax')
midi.instruments.append(sax_instrument)

# -----------------------------
# Bar 1: Little Ray (Drums) - 16th note hi-hat, kick on 1 & 3, snare on 2 & 4
bar_start = 0
bar_end = seconds_per_bar

# Hi-hat on every 16th note
for i in range(0, 16):
    note_time = bar_start + i * seconds_per_beat / 4
    drum_instrument.notes.append(Note(velocity=100, pitch=42, start=note_time, end=note_time + 0.05))

# Kick on 1 and 3
drum_instrument.notes.append(Note(velocity=110, pitch=36, start=bar_start, end=bar_start + 0.1))
drum_instrument.notes.append(Note(velocity=110, pitch=36, start=bar_start + 2 * seconds_per_beat, end=bar_start + 2 * seconds_per_beat + 0.1))

# Snare on 2 and 4
drum_instrument.notes.append(Note(velocity=100, pitch=38, start=bar_start + seconds_per_beat, end=bar_start + seconds_per_beat + 0.1))
drum_instrument.notes.append(Note(velocity=100, pitch=38, start=bar_start + 3 * seconds_per_beat, end=bar_start + 3 * seconds_per_beat + 0.1))

# -----------------------------
# Bar 2-4: Full ensemble
# Start at bar 2 (bar_start = seconds_per_bar)
bar_start = seconds_per_bar
bar_end = 3 * seconds_per_bar

# -----------------------------
# Marcus: Bass - Walking line, chromatic approaches, no repeating notes
# In D minor
bass_line = [50, 49, 51, 52, 50, 49, 51, 52, 50, 49, 51, 52, 50, 49, 51, 52]  # D D# C# D D D# C# D D D# C# D D D# C# D
for i, note in enumerate(bass_line):
    start_time = bar_start + i * seconds_per_beat / 4
    end_time = start_time + 0.1
    bass_instrument.notes.append(Note(velocity=90, pitch=note, start=start_time, end=end_time))

# Diane: Piano - 7th chords on 2 and 4, comping
# D7 (D F# A C)
# G7 (G B D F)
# A7 (A C# E G)
# Bm7 (B D F# A)
chords = [
    (62, 67, 69, 64),  # D7
    (67, 71, 69, 72),  # G7
    (69, 74, 76, 71),  # A7
    (71, 76, 78, 74),  # Bm7
]
for i, chord in enumerate(chords):
    # Play on 2 and 4 (beats 2 and 4 of bar 2, 2 and 4 of bar 3, and 2 and 4 of bar 4)
    # Each chord is played at two beats: 2 and 4
    for j in [1, 3]:
        time = bar_start + i * seconds_per_bar + j * seconds_per_beat
        for pitch in chord:
            piano_instrument.notes.append(Note(velocity=90, pitch=pitch, start=time, end=time + 0.1))

# Dante: Tenor Sax - Melody (4 bars, 1 motif, start and end)
# Motif: D - F# - B - D (D minor)
# Play the motif in bar 2, start on beat 1, end on beat 3, then restate on beat 4 with a twist
# First phrase: D - F# - B - D (starting on beat 1 of bar 2)
sax_notes = [62, 67, 71, 62]  # D - F# - B - D
# Play the first four notes over the first three beats of bar 2
for i, note in enumerate(sax_notes):
    time = bar_start + i * seconds_per_beat + 0.1  # start slightly after the beat
    sax_instrument.notes.append(Note(velocity=105, pitch=note, start=time, end=time + 0.2))

# Repeat the motif but with a chromatic twist (add a chromatic passing tone)
sax_notes_twist = [62, 67, 70, 71, 62]  # D - F# - Bb - B - D
for i, note in enumerate(sax_notes_twist):
    time = bar_start + 3 * seconds_per_beat + i * 0.2  # start on beat 4 of bar 2
    sax_instrument.notes.append(Note(velocity=105, pitch=note, start=time, end=time + 0.2))

# -----------------------------
# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file 'dante_intro.mid' created successfully.")
