
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax takes the melody. Dm7 chord (F, A, C, D)
# Diane plays Dm7 (F, A, C, D) open voicing on beat 2
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=2.625), # D
]
piano.notes.extend(piano_notes)

# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (38) - C (37) - D (38) - F (41)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),
    # Bar 3: F (41) - E (40) - F (41) - A (44)
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),
    # Bar 4: A (44) - G (43) - A (44) - D (38)
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Dante's sax motif: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, E, F, G, A, Bb, C, D
sax_notes = [
    # Bar 2: D, E (start), leave hanging
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # E
    # Bar 3: G, A (continue)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # A
    # Bar 4: Bb, C (finish)
    pretty_midi.Note(velocity=110, pitch=68, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25),  # C
    # Repeat the beginning part at the end to close the motif
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0)   # D
]
sax.notes.extend(sax_notes)

# Add the drum pattern for bar 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
