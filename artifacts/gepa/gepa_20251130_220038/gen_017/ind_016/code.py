
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
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat, drum_kick2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # D
    # Bar 3, beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),
    # Bar 4, beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for i in range(2, 5):
    start = i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every eighth
    for j in range(0, 8):
        pretty_midi.Note(velocity=100, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.1875)

# Sax: Dm motif
# Bar 2, first four notes (D, Eb, C, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
    # Leave it hanging, return in bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
