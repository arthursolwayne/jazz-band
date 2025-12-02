
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75), # Db
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (beat 2)
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # Db
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Bb
    # Bar 3 (beat 2)
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125), # Db
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # Bb
    # Bar 4 (beat 2)
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625), # Db
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # Bb
]
piano.notes.extend(piano_notes)

# Sax (Dante) - one short motif, make it sing
# Start with Fm7 (F, Ab, Bb, Db), then move to G7 (G, Bb, D, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=110, pitch=57, start=1.75, end=2.0),  # Db
    pretty_midi.Note(velocity=110, pitch=55, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=57, start=2.5, end=2.75),  # Db
    pretty_midi.Note(velocity=110, pitch=55, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=110, pitch=58, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=57, start=3.75, end=4.0),  # Db
    pretty_midi.Note(velocity=110, pitch=55, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=68, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # F
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875))
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0))
    # Hihat on every eighth
    for i in range(0, 4):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
