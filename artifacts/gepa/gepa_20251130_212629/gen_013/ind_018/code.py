
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax starts the melody
# Fm chord: F, Ab, C, D, Eb
# Melody: F (0.0), Ab (0.375), C (0.75), rest (1.125)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.625),
]

sax.notes.extend(sax_notes)

# Marcus: Walking bass line in Fm
# F, Gb, E, D, C, Bb, Ab, G
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),
]

bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords
# F7 on 2, Dm7 on 4
# Bar 2 (1.5-3.0): F7 on beat 2
# Bar 3 (3.0-4.5): Dm7 on beat 4
# Bar 4 (4.5-6.0): F7 on beat 2
piano_notes = [
    # Bar 2, beat 2 (F7)
    pretty_midi.Note(velocity=95, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=68, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=74, start=1.875, end=2.25),
    # Bar 3, beat 4 (Dm7)
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=95, pitch=65, start=3.75, end=4.125),
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=95, pitch=70, start=3.75, end=4.125),
    # Bar 4, beat 2 (F7)
    pretty_midi.Note(velocity=95, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=74, start=4.875, end=5.25),
]

piano.notes.extend(piano_notes)

# Bar 1 drum fill
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2-4 drum pattern
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)

# Add drum notes to the instrument
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
