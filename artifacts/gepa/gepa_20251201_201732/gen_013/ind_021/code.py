
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38), chromatic approach to G2 (43)
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.6875),  # chromatic approach
    pretty_midi.Note(velocity=85, pitch=38, start=1.6875, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.0),    # G2
    # Bar 3: G2 (43), chromatic approach to C3 (48)
    pretty_midi.Note(velocity=80, pitch=44, start=2.0, end=2.1875),  # chromatic approach
    pretty_midi.Note(velocity=85, pitch=43, start=2.1875, end=2.375),  # G2
    pretty_midi.Note(velocity=80, pitch=48, start=2.375, end=2.5625), # C3
    # Bar 4: C3 (48), chromatic approach to F3 (53)
    pretty_midi.Note(velocity=80, pitch=49, start=2.5625, end=2.75),  # chromatic approach
    pretty_midi.Note(velocity=85, pitch=48, start=2.75, end=2.9375),  # C3
    pretty_midi.Note(velocity=80, pitch=53, start=2.9375, end=3.125), # F3
    # Bar 5: F3 (53), chromatic approach to Bb3 (58)
    pretty_midi.Note(velocity=80, pitch=54, start=3.125, end=3.3125),  # chromatic approach
    pretty_midi.Note(velocity=85, pitch=53, start=3.3125, end=3.5),  # F3
    pretty_midi.Note(velocity=80, pitch=58, start=3.5, end=3.6875), # Bb3
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=85, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=85, pitch=57, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # C
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.375),  # G
    pretty_midi.Note(velocity=85, pitch=59, start=2.0, end=2.375),  # B
    pretty_midi.Note(velocity=85, pitch=62, start=2.0, end=2.375),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.375),  # F
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=2.5625, end=2.9375),  # C
    pretty_midi.Note(velocity=85, pitch=63, start=2.5625, end=2.9375),  # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=2.5625, end=2.9375),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.5625, end=2.9375),  # Bb
    # Bar 5: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=3.125, end=3.5),  # F
    pretty_midi.Note(velocity=85, pitch=69, start=3.125, end=3.5),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=3.125, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=76, start=3.125, end=3.5),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First phrase: D (62), F (65), Ab (68), Bb (71)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.1875),
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=71, start=2.1875, end=2.375),
    # Come back and finish it
    pretty_midi.Note(velocity=100, pitch=68, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=100, pitch=65, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.9375),
    # Repeat without the Bb, just the motivic idea
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=100, pitch=65, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=100, pitch=65, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0625)
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.9375),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875)
]
drums.notes.extend(bar2_drum_notes)

# Bar 3 and 4: same pattern
for i in range(1.5, 4.0, 1.5):
    for note in drum_notes:
        if note.start < 1.5:
            new_start = note.start + i
            new_end = note.end + i
            new_note = pretty_midi.Note(note.velocity, note.pitch, new_start, new_end)
            drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
