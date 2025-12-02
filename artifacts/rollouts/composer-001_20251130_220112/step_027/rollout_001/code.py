
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=39, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=44, start=5.625, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=42, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=95, pitch=45, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=95, pitch=47, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=95, pitch=49, start=2.25, end=2.625), # F
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=95, pitch=47, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=95, pitch=50, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=95, pitch=52, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=95, pitch=54, start=3.375, end=3.75), # C
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=42, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=95, pitch=45, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=95, pitch=47, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=95, pitch=49, start=4.875, end=5.25), # F
]
piano.notes.extend(piano_notes)

# Sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.6875), # G
    pretty_midi.Note(velocity=110, pitch=50, start=1.6875, end=1.875), # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.1875), # G
    pretty_midi.Note(velocity=110, pitch=50, start=3.1875, end=3.375), # Bb
    # Bar 4: Return and finish it
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.6875), # G
    pretty_midi.Note(velocity=110, pitch=50, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=110, pitch=47, start=4.875, end=5.0625), # Eb
    pretty_midi.Note(velocity=110, pitch=45, start=5.0625, end=5.25), # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),

drums.notes.extend([

])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_wayne.mid")
