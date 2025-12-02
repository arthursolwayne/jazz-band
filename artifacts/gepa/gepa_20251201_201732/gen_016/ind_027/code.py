
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)   # F2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last (Bar 2: Fm7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),    # F4 (root)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),    # A4 (7th)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),    # D4 (5th)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),    # E4 (9th)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # B4 (first note)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # D5 (second note)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # B4 (repeat)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0)   # D5 (resolve)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75), # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125), # Bb2 (5th)
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5)   # A2 (root approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last (Bar 3: Bb7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),    # Bb4 (root)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),    # D4 (7th)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),    # C4 (9th)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5)     # F5 (extensions)
]
piano.notes.extend(piano_notes)

# Sax: Continue motif variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # B4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # D5
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5)   # B4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875),  # A2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)   # F2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last (Bar 4: Fm7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),    # F4 (root)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),    # A4 (7th)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),    # D4 (5th)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0)     # E4 (9th)
]
piano.notes.extend(piano_notes)

# Sax: Continue motif variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # D5
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # B4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0)   # D5
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_introduction.mid')
