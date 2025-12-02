
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F#2 (fifth), E2 (chromatic approach), G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),
    # Bar 3: G2 (root), B2 (fifth), A2 (chromatic approach), B2 (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=46, start=4.125, end=4.5),
    # Bar 4: C3 (root), E3 (fifth), D3 (chromatic approach), E3 (fifth)
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: G7 (G, B, D, F)
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bar 2: Fmaj7
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=80, pitch=58, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=3.0),  # E4
    # Bar 3: G7
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=4.5),  # F4
    # Bar 4: Cm7
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=80, pitch=54, start=4.5, end=6.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 (beat 1), A4 (beat 2), G4 (beat 3), F4 (beat 4)
# Then repeat with a slight variation
sax_notes = [
    # First pass (bar 2)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125),  # F4
    # Second pass (bar 4)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),  # G4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
# Snare on 2 and 4
# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat
    for i in range(0, 4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)

drums.notes.extend([note for note in drum_notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_moment.mid")
