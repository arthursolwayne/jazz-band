
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F, Ab, D, C)
# Bar 2: F - Ab - D - C
# Bar 3: F - Ab - D - C
# Bar 4: F - Ab - D - C
# Chromatic approaches on the downbeats
bass_notes = [
    # Bar 2: F (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),

    # Bar 3: Ab (fifth) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5),

    # Bar 4: D (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=54, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last beat
# Bar 2: Fm7 (F, Ab, C, Eb) -> resolve to C
# Bar 3: Fm7 (F, Ab, C, Eb) -> resolve to Dm7 (D, F, A, C)
# Bar 4: Fm7 (F, Ab, C, Eb) -> resolve to G7 (G, B, D, F)
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=1.875),
    # Resolve to C
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),

    # Bar 3: Fm7
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),
    # Resolve to Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),

    # Bar 4: Fm7
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),
    # Resolve to G7
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - D - C, played on 1 & 3 & 5 in bar 2
sax_notes = [
    # Bar 2: F - Ab - D - C
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=1.975),
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=2.75),

    # Bar 3: F - Ab - D - C
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.475),
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.25),

    # Bar 4: F - Ab - D - C
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=4.975),
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=5.75)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
