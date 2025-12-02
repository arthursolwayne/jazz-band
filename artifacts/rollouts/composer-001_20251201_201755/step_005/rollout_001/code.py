
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Fm (F, Ab, D, Eb) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25), # Gb2 (Ab)
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625), # Bb2 (D?)
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),  # Eb2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=2.0),   # Ab2
    pretty_midi.Note(velocity=80, pitch=58, start=1.5, end=2.0),   # C3
    pretty_midi.Note(velocity=90, pitch=56, start=1.5, end=2.0),   # Eb3
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.5),  # Bb2
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.5),   # D3
    pretty_midi.Note(velocity=80, pitch=53, start=2.0, end=2.5),   # F2
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.5),   # Ab2
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=56, start=2.5, end=3.0),  # Eb2
    pretty_midi.Note(velocity=90, pitch=61, start=2.5, end=3.0),   # G3
    pretty_midi.Note(velocity=80, pitch=58, start=2.5, end=3.0),   # Bb2
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0),   # D3
])
piano.notes.extend(piano_notes)

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging.
# Motif: F, Gb, Ab, Bb (motif: 63, 60, 62, 65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=63, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=105, pitch=60, start=1.75, end=2.0),  # Gb3
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Ab3
    pretty_midi.Note(velocity=95, pitch=65, start=2.25, end=2.5),   # Bb3
]
# Leave it hanging, come back later
sax_notes.append(pretty_midi.Note(velocity=90, pitch=63, start=2.5, end=2.75))
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (3.0 - 6.0s)
# Marcus: Walking bass line in Fm (F, Ab, D, Eb) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # Eb2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.5),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.5),   # Ab2
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.5),   # C3
    pretty_midi.Note(velocity=90, pitch=56, start=3.0, end=3.5),   # Eb3
]
piano.notes.extend(piano_notes)

# Dante: Return to complete the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=63, start=3.5, end=3.75),  # F3
    pretty_midi.Note(velocity=105, pitch=60, start=3.75, end=4.0),  # Gb3
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # Ab3
    pretty_midi.Note(velocity=95, pitch=65, start=4.25, end=4.5),   # Bb3
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
