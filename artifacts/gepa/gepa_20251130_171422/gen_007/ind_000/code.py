
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time in seconds: 0.0 to 1.5
bar_length = 1.5
time = 0.0

# Kick on 1 and 3
kick_times = [0.0, bar_length * 1.5]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [bar_length * 0.5, bar_length * 2.0]
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

# Hihat on every eighth note (0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625)
hihat_times = [time + i * 0.375 for i in range(4)]
for t in hihat_times:
    note = pretty_midi.Note(velocity=90, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Time starts at 1.5s
time = 1.5

# Bass line: walking line with chromatic approaches
# D (D, F#, A, C#) -> Dm7 -> G7 -> Cmaj7 -> F7 -> Bm7 -> E7 -> A7 -> Dm7

# Bass line in D minor, chromatic approaches on certain notes
# Root movement: D -> C# -> B -> A -> G -> F# -> E -> D

# Bass notes (in quarter notes)
bass_notes = [
    (1.5, 50),   # D
    (1.75, 49),  # C#
    (2.25, 48),  # B
    (2.75, 47),  # A
    (3.25, 46),  # G
    (3.75, 45),  # F#
    (4.25, 44),  # E
    (4.75, 50),  # D
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: comping on 2 and 4 with 7th chords
# Dm7 (D, F, A, C)
# G7 (G, B, D, F)
# Cmaj7 (C, E, G, B)
# F7 (F, A, C, E♭)

# Time grid: 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0
comp_times = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]

comp_chords = [
    (1.5, [50, 53, 57, 60]),  # Dm7
    (2.0, [62, 67, 69, 64]),  # G7
    (2.5, [60, 64, 67, 71]),  # Cmaj7
    (3.0, [65, 69, 72, 67]),  # F7
    (3.5, [50, 53, 57, 60]),  # Dm7
    (4.0, [62, 67, 69, 64]),  # G7
    (4.5, [60, 64, 67, 71]),  # Cmaj7
    (5.0, [65, 69, 72, 67]),  # F7
    (5.5, [50, 53, 57, 60]),  # Dm7
]

for start, pitches in comp_chords:
    for pitch in pitches:
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.5)
        piano.notes.append(note)

# Saxophone motif: haunting, melodic, single line
# Start at 1.5s with a short motif: D (50), F# (53), B (57), rest
# Then repeat with some variation at 3.0s, ending on D (50)

# First motif
note1 = pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=100, pitch=53, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=100, pitch=57, start=2.0, end=2.25)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)

# Second motif: same idea, start on A (57), then D (50), F# (53), B (57), then rest
note4 = pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25)
note5 = pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.5)
note6 = pretty_midi.Note(velocity=100, pitch=53, start=3.5, end=3.75)
note7 = pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0)
sax.notes.append(note4)
sax.notes.append(note5)
sax.notes.append(note6)
sax.notes.append(note7)

# Final note: D (50) on the "and" of 4, just before the end
note8 = pretty_midi.Note(velocity=100, pitch=50, start=5.75, end=6.0)
sax.notes.append(note8)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
