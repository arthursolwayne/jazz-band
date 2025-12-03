
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A2 on 3
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # C2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25),  # C5

    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=3.0),  # F5

    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # C5
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.75),  # Eb5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),  # Bb5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # A4 on 1
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # C5 on 2
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.875), # B4 on 3 (half note)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # A4 on 4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums continue with same pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # F2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # A2 on 3
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # C2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.75),  # F5

    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.5),  # Eb5
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),  # G5
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.5),  # Bb5
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # A4 on 1
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # C5 on 2
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.375), # B4 on 3 (half note)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # A4 on 4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums continue with same pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # F2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # A2 on 3
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # C2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25),  # C5
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=5.25),  # Eb5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # G5
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.25),  # Bb5
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # A4 on 1
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # C5 on 2
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.875), # B4 on 3 (half note)
    pretty_midi.Note(velocity=100, pitch=62, start=6.0, end=6.375),  # A4 on 4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
