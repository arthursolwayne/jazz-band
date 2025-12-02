
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on beat 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on beat 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for i in range(8):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm7 -> F -> G -> Bb -> Dm7 (play D, F, G, Bb over 4 bars, spaced out)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.0 + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=6.0, end=6.0 + 0.375),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.5 + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=1.875 + 0.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.25 + 0.375),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=2.625 + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.0 + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.375 + 0.375),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=3.75 + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.125 + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=4.5, end=4.5 + 0.375),  # G
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=4.875 + 0.375),  # G#
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.25 + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=5.625, end=5.625 + 0.375),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + 0.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.5 + 0.375),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + 0.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.5 + 0.375),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.0 + 0.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.0 + 0.375),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.0 + 0.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.0 + 0.375),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.5 + 0.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.5 + 0.375),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.5 + 0.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.5 + 0.375),  # F
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on beat 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on beat 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=start + beat * 0.375, end=start + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for i in range(8):
        note = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.05)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
