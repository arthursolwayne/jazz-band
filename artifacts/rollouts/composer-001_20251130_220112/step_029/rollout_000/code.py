
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

# Bass line: Marcus - walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=90, pitch=44, start=1.875, end=2.0625), # E
    pretty_midi.Note(velocity=90, pitch=43, start=2.0625, end=2.25), # Eb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=90, pitch=41, start=3.1875, end=3.375), # Db
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=90, pitch=39, start=3.5625, end=3.75), # Bb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=4.6875, end=4.875), # F#
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.0625), # E
    pretty_midi.Note(velocity=90, pitch=43, start=5.0625, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375), # D
    pretty_midi.Note(velocity=90, pitch=41, start=5.4375, end=5.625), # Db
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=5.8125), # C
    pretty_midi.Note(velocity=90, pitch=39, start=5.8125, end=6.0), # Bb
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - 7th chord on beat 2
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.0),  # C
    # Bar 3 (3.0 - 4.5s) - 7th chord on beat 2
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.5625),  # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.5625),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.5625),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.5625),  # C
    # Bar 4 (4.5 - 6.0s) - 7th chord on beat 2
    pretty_midi.Note(velocity=80, pitch=43, start=5.1875, end=5.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=5.1875, end=5.375),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=5.1875, end=5.375),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=5.1875, end=5.375),  # C
]
piano.notes.extend(piano_notes)

# Sax: Dante - motif in Fm
sax_notes = [
    # Bar 2 (1.5 - 3.0s) - motif starts
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875), # F (Bb)
    pretty_midi.Note(velocity=110, pitch=63, start=1.6875, end=1.875), # Eb (Ab)
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0625), # G (B)
    pretty_midi.Note(velocity=110, pitch=61, start=2.0625, end=2.25), # D (F)
    # Bar 3 (3.0 - 4.5s) - motif returns
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.1875), # F (Bb)
    pretty_midi.Note(velocity=110, pitch=63, start=3.1875, end=3.375), # Eb (Ab)
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.5625), # G (B)
    pretty_midi.Note(velocity=110, pitch=61, start=3.5625, end=3.75), # D (F)
    # Bar 4 (4.5 - 6.0s) - motif resolves
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.6875), # F (Bb)
    pretty_midi.Note(velocity=110, pitch=63, start=4.6875, end=4.875), # Eb (Ab)
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.0625), # G (B)
    pretty_midi.Note(velocity=110, pitch=61, start=5.0625, end=5.25), # D (F)
    # Final resolution
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.4375), # E (Ab)
    pretty_midi.Note(velocity=110, pitch=59, start=5.4375, end=5.625), # D (G)
    pretty_midi.Note(velocity=110, pitch=57, start=5.625, end=5.8125), # Bb (D)
    pretty_midi.Note(velocity=110, pitch=55, start=5.8125, end=6.0), # G (Bb)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2])
# Snare on 2 and 4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.extend([snare1, snare2])
# Hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
