
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36, 100), # kick on 1
    (0.375, 42, 80), # hihat
    (0.75, 38, 100), # snare on 2
    (1.125, 42, 80), # hihat
    (1.5, 36, 100), # kick on 3
    (1.875, 42, 80), # hihat
    (2.25, 38, 100), # snare on 4
    (2.625, 42, 80), # hihat
]

for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 45, 60), # Fm7 - F
    (1.875, 46, 60), # Gb
    (2.25, 44, 60), # Eb
    (2.625, 45, 60), # F
    (3.0, 48, 60), # Ab
    (3.375, 47, 60), # G
    (3.75, 46, 60), #Gb
    (4.125, 45, 60), # F
    (4.5, 49, 60), # Bb
    (4.875, 50, 60), # B
    (5.25, 51, 60), # C
    (5.625, 49, 60), # Bb
]

for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.5, 64, 100), # F7 - F
    (1.5, 71, 100), # Bb
    (1.5, 69, 100), # Eb
    (1.5, 76, 100), # Ab
    (1.875, 64, 100),
    (1.875, 71, 100),
    (1.875, 69, 100),
    (1.875, 76, 100),
    # Bar 3
    (2.25, 64, 100),
    (2.25, 71, 100),
    (2.25, 69, 100),
    (2.25, 76, 100),
    (2.625, 64, 100),
    (2.625, 71, 100),
    (2.625, 69, 100),
    (2.625, 76, 100),
    # Bar 4
    (3.0, 64, 100),
    (3.0, 71, 100),
    (3.0, 69, 100),
    (3.0, 76, 100),
    (3.375, 64, 100),
    (3.375, 71, 100),
    (3.375, 69, 100),
    (3.375, 76, 100),
    (3.75, 64, 100),
    (3.75, 71, 100),
    (3.75, 69, 100),
    (3.75, 76, 100),
    (4.125, 64, 100),
    (4.125, 71, 100),
    (4.125, 69, 100),
    (4.125, 76, 100),
    (4.5, 64, 100),
    (4.5, 71, 100),
    (4.5, 69, 100),
    (4.5, 76, 100),
    (4.875, 64, 100),
    (4.875, 71, 100),
    (4.875, 69, 100),
    (4.875, 76, 100),
]

for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First motif
    (1.5, 66, 100), # F
    (1.625, 64, 100), # Eb
    (1.75, 62, 100), # Db
    (1.875, 66, 100), # F
    (2.0, 66, 100), # F
    (2.125, 64, 100), # Eb
    (2.25, 62, 100), # Db
    (2.375, 66, 100), # F
    (2.5, 66, 100), # F
    (2.625, 64, 100), # Eb
    (2.75, 62, 100), # Db
    (2.875, 60, 100), # Bb
    (3.0, 66, 100), # F
    (3.125, 64, 100), # Eb
    (3.25, 62, 100), # Db
    (3.375, 66, 100), # F
    (3.5, 66, 100), # F
    (3.625, 64, 100), # Eb
    (3.75, 62, 100), # Db
    (3.875, 60, 100), # Bb
]

for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.125))

# Add dynamics and expression to sax
for note in sax.notes:
    note.velocity = 100
    note.start = note.start
    note.end = note.end

# Add dynamics to piano
for note in piano.notes:
    note.velocity = 80

# Add dynamics to bass
for note in bass.notes:
    note.velocity = 80

# Add dynamics to drums
for note in drums.notes:
    note.velocity = 100

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.writeFile("intro_wayne.mid")
