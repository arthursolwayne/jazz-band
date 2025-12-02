
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the tempo (160 BPM)
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
dante_sax = Instrument(program=64)  # Tenor sax
diane_piano = Instrument(program=0)  # Acoustic piano
marcus_bass = Instrument(program=33)  # Double bass
little_ray_drums = Instrument(program=10)  # Acoustic snare

pm.instruments = [dante_sax, diane_piano, marcus_bass, little_ray_drums]

# Helper function to convert bar time to seconds
def bar_to_time(bar):
    return bar * (60.0 / 160) * 4  # 60 sec/min / BPM * 4 beats per bar

# Bar 1: Drums only — sparse, brushed snare on 2 and 4, hihat on eighths
bar1_start = bar_to_time(0)
bar1_end = bar_to_time(1)

# Snare on 2 and 4
snare_notes = [
    Note(60, bar1_start + 0.75, bar1_start + 0.75 + 0.1),
    Note(60, bar1_start + 1.5, bar1_start + 1.5 + 0.1)
]

# Hihat on every eighth note
hihat_notes = []
for i in range(1, 9):
    time = bar1_start + (i * 0.375) - 0.1
    hihat_notes.append(Note(42, time, time + 0.1))

little_ray_drums.notes.extend(snare_notes)
little_ray_drums.notes.extend(hihat_notes)

# Bar 2: Bass enters with walking line (chromatic, no repeats)
bar2_start = bar_to_time(1)
bar2_end = bar_to_time(2)

bass_notes = [
    Note(48, bar2_start + 0.0, bar2_start + 0.25),  # F
    Note(49, bar2_start + 0.25, bar2_start + 0.5),  # Gb
    Note(50, bar2_start + 0.5, bar2_start + 0.75),  # G
    Note(51, bar2_start + 0.75, bar2_start + 1.0),  # Ab
    Note(53, bar2_start + 1.0, bar2_start + 1.25),  # Bb
    Note(55, bar2_start + 1.25, bar2_start + 1.5),  # B
    Note(57, bar2_start + 1.5, bar2_start + 1.75),  # C
    Note(59, bar2_start + 1.75, bar2_start + 2.0),  # D
]

marcus_bass.notes.extend(bass_notes)

# Bar 2: Piano enters with 7th chords on 2 and 4
diane_piano.notes.extend([
    # F7 (F A C Eb) on beat 2
    Note(71, bar2_start + 0.75, bar2_start + 0.75 + 0.25),
    Note(82, bar2_start + 0.75, bar2_start + 0.75 + 0.25),
    Note(77, bar2_start + 0.75, bar2_start + 0.75 + 0.25),
    Note(79, bar2_start + 0.75, bar2_start + 0.75 + 0.25),
    
    # Dissonant note on beat 3 (C#)
    Note(66, bar2_start + 1.125, bar2_start + 1.125 + 0.2),
    
    # F7 again on beat 4
    Note(71, bar2_start + 1.5, bar2_start + 1.5 + 0.25),
    Note(82, bar2_start + 1.5, bar2_start + 1.5 + 0.25),
    Note(77, bar2_start + 1.5, bar2_start + 1.5 + 0.25),
    Note(79, bar2_start + 1.5, bar2_start + 1.5 + 0.25),
])

# Bar 2–3: Tenor sax plays F Eb G – open, searching, unresolved
# Bar starts at 1.0, ends at 2.0
bar2_3_start = bar_to_time(1)
bar2_3_end = bar_to_time(2)

# Start with F (65), Eb (62), G (67)
dante_sax.notes.extend([
    Note(65, bar2_3_start + 0.1, bar2_3_start + 0.25),  # F
    Note(62, bar2_3_start + 0.25, bar2_3_start + 0.35),  # Eb
    Note(67, bar2_3_start + 0.35, bar2_3_start + 0.45),  # G
])

# Bar 3: Bass continues walking
bar3_start = bar_to_time(2)
bar3_end = bar_to_time(3)

bass_notes = [
    Note(60, bar3_start + 0.0, bar3_start + 0.25),  # Eb
    Note(61, bar3_start + 0.25, bar3_start + 0.5),  # F
    Note(62, bar3_start + 0.5, bar3_start + 0.75),  # Gb
    Note(63, bar3_start + 0.75, bar3_start + 1.0),  # G
    Note(65, bar3_start + 1.0, bar3_start + 1.25),  # A
    Note(67, bar3_start + 1.25, bar3_start + 1.5),  # Bb
    Note(69, bar3_start + 1.5, bar3_start + 1.75),  # B
    Note(71, bar3_start + 1.75, bar3_start + 2.0),  # C
]

marcus_bass.notes.extend(bass_notes)

# Bar 3: Piano plays a minor 7th chord on 2 and 4
diane_piano.notes.extend([
    # Fm7 (F Ab C Eb) on beat 2
    Note(71, bar3_start + 0.75, bar3_start + 0.75 + 0.25),
    Note(77, bar3_start + 0.75, bar3_start + 0.75 + 0.25),
    Note(77, bar3_start + 0.75, bar3_start + 0.75 + 0.25),
    Note(79, bar3_start + 0.75, bar3_start + 0.75 + 0.25),
    
    # Dissonant note on beat 3 (C#)
    Note(66, bar3_start + 1.125, bar3_start + 1.125 + 0.2),
    
    # Fm7 again on beat 4
    Note(71, bar3_start + 1.5, bar3_start + 1.5 + 0.25),
    Note(77, bar3_start + 1.5, bar3_start + 1.5 + 0.25),
    Note(77, bar3_start + 1.5, bar3_start + 1.5 + 0.25),
    Note(79, bar3_start + 1.5, bar3_start + 1.5 + 0.25),
])

# Bar 4: Sax ends on G, unresolved
bar4_start = bar_to_time(3)
bar4_end = bar_to_time(4)

# G on the last beat
dante_sax.notes.append(Note(67, bar4_start + 1.5, bar4_start + 1.6))

# Save the MIDI file
pm.write("dante_intro.mid")
