
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 4):
    kick_start = 1.5 + i * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    snare_start = kick_start + 0.75
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375)
    for j in range(4):
        hihat_start = kick_start + j * 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.375)
        drums.notes.append(hihat)
    drums.notes.extend([kick, snare])

# Sax (Dante): One short motif, start, leave it hanging, come back and finish it
# Motif: Dm7 (F, A, Bb, D) -> Bb, D, F, A -> D, F, Bb, A
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
