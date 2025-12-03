
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 - G2, root on 1, chromatic approach on 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.125),
    pretty_midi.Note(velocity=80, pitch=38, start=2.125, end=2.5),
    pretty_midi.Note(velocity=80, pitch=40, start=2.5, end=2.875),
    # Bar 3: A2 - D3, root on 1, chromatic approach on 2
    pretty_midi.Note(velocity=80, pitch=45, start=2.875, end=3.25),
    pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=45, start=3.5, end=3.875),
    pretty_midi.Note(velocity=80, pitch=47, start=3.875, end=4.25),
    # Bar 4: B2 - F3, root on 1, chromatic approach on 2
    pretty_midi.Note(velocity=80, pitch=46, start=4.25, end=4.625),
    pretty_midi.Note(velocity=80, pitch=48, start=4.625, end=4.875),
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    # Bar 3: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=74, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=76, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.875, end=3.25),
    # Bar 4: Bm7 (B, D, F#, A)
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.625),
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.625),
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.625),
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.625),
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.0),
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.875, end=3.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.5),
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.25, end=4.625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.625, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=5.0),
])
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # E5
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.125),  # G5
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.5),   # D5
]
# Bar 3: Leave it hanging
sax_notes.append(pretty_midi.Note(velocity=110, pitch=65, start=2.875, end=3.25))  # E5
# Bar 4: Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.625),  # G5
    pretty_midi.Note(velocity=110, pitch=62, start=4.625, end=5.0),   # D5
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
