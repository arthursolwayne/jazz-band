
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root) and C (fifth)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # C3
    # Chromatic approach to G2
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.0),   # F#2
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.375),  # G2
    # Bar 3: G2 and D3
    pretty_midi.Note(velocity=100, pitch=58, start=2.375, end=2.75),  # G2
    pretty_midi.Note(velocity=100, pitch=63, start=2.375, end=2.75),  # D3
    # Chromatic approach to A2
    pretty_midi.Note(velocity=90, pitch=59, start=2.75, end=3.0),    # G#2
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # A2
    # Bar 4: A2 and E3
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # A2
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # E3
    # Chromatic approach to B2
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=4.0),    # A#2
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.375)   # B2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=58, start=2.375, end=2.75),
    pretty_midi.Note(velocity=100, pitch=63, start=2.375, end=2.75),
    pretty_midi.Note(velocity=100, pitch=65, start=2.375, end=2.75),
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.75),
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    # Resolving notes on the last beat of each bar
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0)
]
piano.notes.extend(piano_notes)

# Sax (Dante): Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.125), # B4
    pretty_midi.Note(velocity=110, pitch=64, start=2.125, end=2.375), # G4
    # Bar 3: Motif continues
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.75),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),    # B4
    # Bar 4: Motif resolves
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),    # B4
    # Hold on
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.375)   # B4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bars 2-3: Same pattern as bar 1, repeated
for start in [1.5, 3.0]:
    for note in drum_notes:
        new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + start, note.end + start)
        drums.notes.append(new_note)

# Bar 4: Same kick and snare, but no hihat on last beat
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0)
]
drums.notes.extend(drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
