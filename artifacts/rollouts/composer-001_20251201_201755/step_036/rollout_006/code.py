
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F (fifth with chromatic approach)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.125),
    # G2 (root)
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    # Bb (fifth with chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=2.5, end=2.875)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # A (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # C (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0)   # Eb (MIDI 64)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # Bb (MIDI 62)
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.125), # D (MIDI 65)
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.5),  # Bb (MIDI 62)
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.875)   # D (MIDI 65)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Eb (root)
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),
    # G (fifth with chromatic approach)
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.625),
    # A (root)
    pretty_midi.Note(velocity=90, pitch=49, start=3.625, end=4.0),
    # C (fifth with chromatic approach)
    pretty_midi.Note(velocity=90, pitch=52, start=4.0, end=4.375)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb D F A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),  # Bb (MIDI 58)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=4.5)   # A (MIDI 70)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # D (MIDI 65)
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.75), # F (MIDI 68)
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125), # D (MIDI 65)
    pretty_midi.Note(velocity=110, pitch=68, start=4.125, end=4.5)   # F (MIDI 68)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # C (root)
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),
    # Eb (fifth with chromatic approach)
    pretty_midi.Note(velocity=90, pitch=54, start=4.875, end=5.125),
    # D (root)
    pretty_midi.Note(velocity=90, pitch=49, start=5.125, end=5.5),
    # F (fifth with chromatic approach)
    pretty_midi.Note(velocity=90, pitch=52, start=5.5, end=5.875)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fm7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # A (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # C (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0)   # Eb (MIDI 64)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # Bb (MIDI 62)
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25), # D (MIDI 65)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # Bb (MIDI 62)
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0)   # D (MIDI 65)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
