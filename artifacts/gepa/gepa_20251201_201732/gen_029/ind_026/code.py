
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass (F2 - C3, MIDI 53 - 58), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    # F2 -> E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.25),
    # C3 (fifth)
    pretty_midi.Note(velocity=90, pitch=58, start=2.25, end=2.625),
    # C3 -> D3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb) - open voicing (F, C, Eb, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # Eb5
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875),  # Ab5
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging.
# Fm scale (F, Gb, Ab, A, Bb, B, C) - phrase: F, Ab, Bb, F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # Ab4
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass (F2 - C3, MIDI 53 - 58), roots and fifths with chromatic approaches
# Bbm7 (Bb, Db, F, Ab) - root: Bb2 (58-1=57), fifth: F3 (58+7=65, but in Fm, stay in Fm range)
bass_notes = [
    # Bb2 (root)
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),
    # Bb2 -> A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=56, start=3.375, end=3.75),
    # F3 (fifth, but in Fm context)
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.125),
    # F3 -> Gb3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=59, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Diane on piano: Bbm7 (Bb, Db, F, Ab) - open voicing (Bb, F, Ab, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # Ab5
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),  # Db5
]
piano.notes.extend(piano_notes)

# Dante on sax: Motif continuation, leave it hanging
# Bbm7 motif: Bb, Ab, F, Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # Ab4
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass (F2 - C3, MIDI 53 - 58), roots and fifths with chromatic approaches
# D7alt (D, F, Ab, C) - root: D2 (53+2=55), fifth: A3 (55+7=62)
bass_notes = [
    # D2 (root)
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),
    # D2 -> C2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=54, start=4.875, end=5.25),
    # A3 (fifth, but in Fm context)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),
    # A3 -> Bb3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Diane on piano: D7alt (D, F, Ab, C) - open voicing (D, C, Ab, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # Ab5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F5
]
piano.notes.extend(piano_notes)

# Dante on sax: Motif resolution
# D7alt motif: D, Ab, F, D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # Ab4 (same pitch, but with bend or articulation)
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D4
]
sax.notes.extend(sax_notes)

# Drums for bar 3 and 4
# Same pattern repeated
for bar in [3.0, 4.5]:
    drum_notes = [
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=bar, end=bar + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=bar + 1.125, end=bar + 1.5),
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=bar + 0.75, end=bar + 1.125),
        pretty_midi.Note(velocity=110, pitch=38, start=bar + 1.875, end=bar + 2.25),
        # Hi-hat on every eighth
        pretty_midi.Note(velocity=90, pitch=42, start=bar, end=bar + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 0.375, end=bar + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 0.75, end=bar + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 1.125, end=bar + 1.5),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 1.5, end=bar + 1.875),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 1.875, end=bar + 2.25),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 2.25, end=bar + 2.625),
        pretty_midi.Note(velocity=90, pitch=42, start=bar + 2.625, end=bar + 3.0),
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
