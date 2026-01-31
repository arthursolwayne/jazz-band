
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line in Fm (F, Ab, D, Eb) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.625),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0),  # D2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F3
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # C3
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # D3
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # Bb3
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0),  # D3
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # F3
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=3.0),  # Ab2
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),  # Eb3
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),  # G3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # Bb3
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # D3
]
piano.notes.extend(piano_notes)

# Dante: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=73, start=1.5, end=1.75),  # G3
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),   # F3
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=73, start=2.0, end=2.25),  # G3
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),   # F3
    # Bar 4: Return and finish it
    pretty_midi.Note(velocity=110, pitch=73, start=3.0, end=3.25),  # G3
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.5),   # F3
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),   # D3
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line in Fm (F, Ab, D, Eb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # Eb2
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.125),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=68, start=4.125, end=4.5),   # D2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # Bb3
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # D3
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # F3
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.75),  # Ab2
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.5),  # Eb3
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.5),  # G3
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),  # Bb3
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5),  # D3
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line in Fm (F, Ab, D, Eb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=6.0),   # D2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.25),  # Eb3
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.25),  # G3
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # Bb3
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # D3
]
piano.notes.extend(piano_notes)

# Dante: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # D3
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0),   # F3
    pretty_midi.Note(velocity=110, pitch=73, start=5.0, end=5.25),  # G3
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Bar 3: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
