
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
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on 2
    (1.125, 38, 100), # Snare on 3
    (1.5, 42, 100),  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 43, 100), (1.75, 42, 100), (2.0, 40, 100), (2.25, 38, 100),  # Fm walk
    (2.5, 39, 100), (2.75, 37, 100), (3.0, 38, 100), (3.25, 40, 100),
    (3.5, 42, 100), (3.75, 43, 100), (4.0, 41, 100), (4.25, 39, 100),
    (4.5, 40, 100), (4.75, 38, 100), (5.0, 40, 100), (5.25, 42, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords on 2 and 4, comp on Fm7, Bbm7, Ebm7, Abm7
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    (1.5, 64, 100), (1.5, 69, 100), (1.5, 71, 100), (1.5, 76, 100),  # Fm7
    # Bar 3 (2.5 - 3.0s)
    (2.5, 60, 100), (2.5, 65, 100), (2.5, 67, 100), (2.5, 72, 100),  # Bbm7
    # Bar 4 (3.5 - 4.0s)
    (3.5, 57, 100), (3.5, 62, 100), (3.5, 64, 100), (3.5, 69, 100),  # Ebm7
    # Bar 4 (4.5 - 5.0s)
    (4.5, 52, 100), (4.5, 57, 100), (4.5, 59, 100), (4.5, 64, 100)   # Abm7
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36, 100), (1.75, 42, 100), (2.0, 38, 100), (2.25, 42, 100),
    (2.5, 36, 100), (2.75, 42, 100), (3.0, 38, 100), (3.25, 42, 100),
    (3.5, 36, 100), (3.75, 42, 100), (4.0, 38, 100), (4.25, 42, 100),
    (4.5, 36, 100), (4.75, 42, 100), (5.0, 38, 100), (5.25, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 63, 100), (1.625, 67, 100), (1.75, 63, 100), (2.0, 63, 100),  # F - Bb - F - F
    (2.5, 63, 100), (2.625, 67, 100), (2.75, 63, 100), (3.0, 63, 100),  # F - Bb - F - F
    (3.5, 63, 100), (3.625, 67, 100), (3.75, 63, 100), (4.0, 63, 100),  # F - Bb - F - F
    (4.5, 63, 100), (4.625, 67, 100), (4.75, 63, 100), (5.0, 63, 100)   # F - Bb - F - F
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
