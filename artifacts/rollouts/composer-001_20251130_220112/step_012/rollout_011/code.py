
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.0),
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

# Bars 2-4 (1.5 - 6.0s)
# Bar 2: sax starts with a short motif in F minor
# F Gm7 Bbm7 Eb7
# F (F), Bb (Bb), Eb (Eb), G (G) - short and hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F (tenor sax)
    pretty_midi.Note(velocity=100, pitch=76, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=73, start=2.0, end=2.125),   # Eb
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.375),  # G
]
sax.notes.extend(sax_notes)

# Bass: walking line in F minor
# F, G, Ab, A, Bb, B, C, Db
# Bar 2: F -> G -> Ab -> A (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=47, start=1.5, end=1.625),
    pretty_midi.Note(velocity=70, pitch=48, start=1.625, end=1.75),
    pretty_midi.Note(velocity=70, pitch=45, start=1.75, end=1.875),
    pretty_midi.Note(velocity=70, pitch=46, start=1.875, end=2.0),
    pretty_midi.Note(velocity=70, pitch=47, start=2.0, end=2.125),
    pretty_midi.Note(velocity=70, pitch=48, start=2.125, end=2.25),
    pretty_midi.Note(velocity=70, pitch=49, start=2.25, end=2.375),
    pretty_midi.Note(velocity=70, pitch=46, start=2.375, end=2.5)
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4 with 7th chords
# F7 on 2, Bbm7 on 4
# Bar 2: F7 at beat 2, Bbm7 at beat 4
piano_notes = [
    # F7: F, A, C, E
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=68, start=1.75, end=1.875),  # E
    # Bbm7: Bb, D, F, Ab
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.375),  # Ab
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Start from 1.5s to 3.0s (bar 2)
for i in range(2):
    start = 1.5 + (i * 1.5)
    drum_notes = [
        pretty_midi.Note(velocity=90, pitch=36, start=start + 0.0, end=start + 0.375),  # Kick 1
        pretty_midi.Note(velocity=90, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick 3
        pretty_midi.Note(velocity=95, pitch=38, start=start + 0.75, end=start + 0.875),  # Snare 2
        pretty_midi.Note(velocity=95, pitch=38, start=start + 1.875, end=start + 2.0),  # Snare 4
        # Hihat on every eighth
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5)
    ]
    drums.notes.extend(drum_notes)

# Bar 4: Drums continue
# Same pattern as bar 3
for i in range(2):
    start = 3.0 + (i * 1.5)
    drum_notes = [
        pretty_midi.Note(velocity=90, pitch=36, start=start + 0.0, end=start + 0.375),  # Kick 1
        pretty_midi.Note(velocity=90, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick 3
        pretty_midi.Note(velocity=95, pitch=38, start=start + 0.75, end=start + 0.875),  # Snare 2
        pretty_midi.Note(velocity=95, pitch=38, start=start + 1.875, end=start + 2.0),  # Snare 4
        # Hihat on every eighth
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5)
    ]
    drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
