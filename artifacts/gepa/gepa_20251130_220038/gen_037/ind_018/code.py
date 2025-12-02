
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
drum_hihat = pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=61, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane - Piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # D

    # Bar 3: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # D

    # Bar 4: Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # D
]
piano.notes.extend(piano_notes)

# Little Ray - Drums (Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    start = 1.5 * bar
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    drums.notes.extend([kick, snare, hihat])

# Dante - Saxophone (melody: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
# Motif: D - F - Eb - C (whisper), then D - F - Eb - D (cry)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # C

    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
