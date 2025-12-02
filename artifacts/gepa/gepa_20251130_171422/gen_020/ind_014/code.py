
import pretty_midi

# Create a new MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# ----------------------------
# Bar 1: Little Ray alone (0.0 - 1.5s) - 4/4 time, 160 BPM = 0.375s per beat
# Build tension with snare and hihat, kick on 1 and 3
# ----------------------------
# Bar: 0.0s - 1.5s
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=1.125, end=1.5))

drums.notes.append(pretty_midi.Note(velocity=110, pitch=snare, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=snare, start=1.125, end=1.25))

drums.notes.append(pretty_midi.Note(velocity=120, pitch=kick, start=0.0, end=0.125))
drums.notes.append(pretty_midi.Note(velocity=120, pitch=kick, start=0.75, end=0.875))

# ----------------------------
# Bars 2-4: Full quartet (1.5 - 6.0s)

# Key: Fm (F, Ab, Bb, C, Eb, G, A)
# Time signature: 4/4, 160 BPM

# Bass line: Marcus - walking line, chromatic approaches, never the same note twice.
# Fm7 = F, Ab, Bb, D
# Starting on Eb (chromatic approach to F)
bass_notes = [
    (1.5, 57),  # Eb (chromatic approach to F)
    (1.75, 59),  # F
    (2.0, 60),  # G (chromatic approach to Ab)
    (2.25, 62),  # Ab
    (2.5, 60),  # G
    (2.75, 62),  # Ab
    (3.0, 57),  # Eb (chromatic approach to F)
    (3.25, 59),  # F
    (3.5, 60),  # G
    (3.75, 62),  # Ab
    (4.0, 60),  # G
    (4.25, 62),  # Ab
    (4.5, 60),  # G
    (4.75, 62),  # Ab
    (5.0, 60),  # G
    (5.25, 62),  # Ab
    (5.5, 57),  # Eb
    (5.75, 59),  # F
]

for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25))

# Piano: Diane - 7th chords, comp on 2 and 4, moving with emotion
# Fm7 (F, Ab, Bb, D)
piano_notes = [
    # Bar 2 - 2 and 4
    (2.0, 66), (2.0, 68), (2.0, 70), (2.0, 73),  # Fm7
    (2.5, 66), (2.5, 68), (2.5, 70), (2.5, 73),  # Fm7
    # Bar 3 - 2 and 4
    (3.0, 66), (3.0, 68), (3.0, 70), (3.0, 73),  # Fm7
    (3.5, 66), (3.5, 68), (3.5, 70), (3.5, 73),  # Fm7
    # Bar 4 - 2 and 4
    (4.0, 66), (4.0, 68), (4.0, 70), (4.0, 73),  # Fm7
    (4.5, 66), (4.5, 68), (4.5, 70), (4.5, 73),  # Fm7
]

for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25))

# Saxophone: Dante - short, emotional motif. Start it, leave it hanging, return to finish it.
# Saxophone motif: F, Bb, Ab, C
# Bar 2: F, Bb
# Bar 3: Ab, C
# Bar 4: F, Bb, Ab, C
sax_notes = [
    (1.5, 66),  # F
    (2.0, 66),  # F (hold)
    (2.25, 69),  # Bb
    (2.5, 69),  # Bb (hold)
    (2.75, 67),  # Ab
    (3.0, 67),  # Ab (hold)
    (3.25, 72),  # C
    (3.5, 72),  # C (hold)
    (3.75, 66),  # F
    (4.0, 66),  # F (hold)
    (4.25, 69),  # Bb
    (4.5, 67),  # Ab
    (4.75, 72),  # C
    (5.0, 72),  # C (hold)
]

for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
