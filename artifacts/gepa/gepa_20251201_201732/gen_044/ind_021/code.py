
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus (Bass): Walking line with chromatic approaches, D2-G2 (MIDI 38-43)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.125), # C#2
    pretty_midi.Note(velocity=90, pitch=40, start=2.125, end=2.5), # D2
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.875), # G2

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.875, end=3.25), # G2
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.5), # F#2
    pretty_midi.Note(velocity=90, pitch=43, start=3.5, end=3.875), # G2
    pretty_midi.Note(velocity=90, pitch=40, start=3.875, end=4.25), # D2

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=40, start=4.25, end=4.625), # D2
    pretty_midi.Note(velocity=90, pitch=39, start=4.625, end=4.875), # C#2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # D2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # G2
]
bass.notes.extend(bass_notes)

# Diane (Piano): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0), # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0), # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0), # Eb5

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0), # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0), # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0), # F5
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0), # Ab5

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=4.0), # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0), # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0), # G5
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0), # Bb5
]
piano.notes.extend(piano_notes)

# Dante (Sax): One short motif, haunting, incomplete
# Fm scale: F, Gb, Ab, A, Bb, B, C
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75), # F5
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0), # Ab5

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=72, start=2.5, end=2.75), # F5
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0), # Ab5

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75), # F5
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0), # Ab5
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25), # Bb5
    pretty_midi.Note(velocity=110, pitch=72, start=4.25, end=4.5), # F5
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
drum_notes_bar2 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes_bar2)

drum_notes_bar3 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0625, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.4375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=3.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.8125, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.1875, end=4.375),
]
drums.notes.extend(drum_notes_bar3)

drum_notes_bar4 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.75),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.9375, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.3125, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.6875, end=5.875),
]
drums.notes.extend(drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('jazz_intro.mid')
