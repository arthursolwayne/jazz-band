
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_pattern = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat
]

for note in drum_pattern:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# Fm7 -> Bb7 -> Eb7 -> Am7 -> Dm7 -> Gm7 -> Cm7 -> Fm7
bass_notes = [36, 37, 35, 34, 36, 37, 35, 34, 36, 37, 35, 34, 36, 37, 35, 34]
bass_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625, 6.0, 6.375, 6.75, 7.125]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Diane: 7th chords, comp on 2 and 4
# Fm7 (F, Ab, Bb, D)
piano_notes = [
    (1.5, 72), (1.5, 70), (1.5, 69), (1.5, 67),  # Fm7
    (2.625, 72), (2.625, 70), (2.625, 69), (2.625, 67),  # Fm7
    (3.75, 72), (3.75, 70), (3.75, 69), (3.75, 67),  # Fm7
    (4.875, 72), (4.875, 70), (4.875, 69), (4.875, 67),  # Fm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0)
drum_pattern = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat
]
for note in drum_pattern:
    drums.notes.append(note)

# Bar 3 (3.0 - 4.5)
drum_pattern = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat
]
for note in drum_pattern:
    drums.notes.append(note)

# Bar 4 (4.5 - 6.0)
drum_pattern = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat
]
for note in drum_pattern:
    drums.notes.append(note)

# Dante: Tenor sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, Bb, B, C, Db
# Motif: F, Ab, Bb, F (hanging on the third beat), then C, Ab, Bb, F

sax_notes = [
    (1.5, 72), (1.875, 70), (2.25, 69), (2.625, 72),  # F, Ab, Bb, F
    (3.0, 72), (3.375, 70), (3.75, 69), (4.125, 72),  # F, Ab, Bb, F
    (4.5, 72), (4.875, 70), (5.25, 69), (5.625, 72)   # F, Ab, Bb, F
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('waynes_moment.mid')
