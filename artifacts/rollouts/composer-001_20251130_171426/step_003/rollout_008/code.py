
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
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    (1.5, 47), # F
    (1.75, 48), # Gb
    (2.0, 46), # E
    (2.25, 47), # F
    (2.5, 48), # Gb
    (2.75, 49), # Ab
    (3.0, 47), # F
    (3.25, 48), # Gb
    (3.5, 50), # Bb
    (3.75, 47), # F
    (4.0, 48), # Gb
    (4.25, 46), # E
    (4.5, 47), # F
    (4.75, 48), # Gb
    (5.0, 50), # Bb
    (5.25, 47), # F
    (5.5, 48), # Gb
    (5.75, 46), # E
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 59), # F7 (C, E, G, Bb)
    (2.0, 57), # C
    (2.0, 60), # E
    (2.0, 62), # G
    (2.0, 61), # Bb
    # Bar 3
    (3.0, 59), # F7
    (3.0, 57), # C
    (3.0, 60), # E
    (3.0, 62), # G
    (3.0, 61), # Bb
    # Bar 4
    (4.0, 59), # F7
    (4.0, 57), # C
    (4.0, 60), # E
    (4.0, 62), # G
    (4.0, 61), # Bb
]

for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25)
    piano.notes.append(note)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Gb, E, F (in 8th notes)
sax_notes = [
    (1.5, 66), # F
    (1.75, 67), # Gb
    (2.0, 64), # E
    (2.25, 66), # F
    (3.0, 66), # F (return)
    (3.25, 67), # Gb
    (3.5, 64), # E
    (3.75, 66), # F
]

for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=t, end=t + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
