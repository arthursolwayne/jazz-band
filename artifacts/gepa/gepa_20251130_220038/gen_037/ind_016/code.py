
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),    # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=83, start=1.5, end=1.75),  # E
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=80, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=83, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.5),  # Ab
    # Bar 4: F7 again
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=83, start=3.0, end=3.25),  # E
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start_time = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.125, end=start_time + 1.5)
    hihat = [
        pretty_midi.Note(velocity=100, pitch=42, start=start_time, end=start_time + 0.375),
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125),
        pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5),
    ]
    drums.notes.extend([kick, snare, kick2, snare2] + hihat)

# Saxophone: Whisper to cry motif (bars 2-4)
# Bar 2: A flat (Diatonic 2nd of F minor)
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=83, start=1.5, end=1.75),  # Ab
    # Bar 3: F minor 7th chord (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=79, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=83, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=77, start=2.5, end=2.75),  # C
    # Bar 4: C minor 7th (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=81, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=83, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=80, start=3.75, end=4.0),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
