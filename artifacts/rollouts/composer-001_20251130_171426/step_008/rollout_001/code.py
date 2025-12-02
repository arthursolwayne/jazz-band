
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # Fm root
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25), # Fm b9
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # Fm 9
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),   # Fm root
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375),  # Fm b7
    pretty_midi.Note(velocity=80, pitch=48, start=3.375, end=3.75), # Fm root
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),  # Fm 9
    pretty_midi.Note(velocity=80, pitch=47, start=4.125, end=4.5),   # Fm b7
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # Fm root
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25), # Fm b9
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),  # Fm 9
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),   # Fm root
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # Ab
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm, short and singable
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Db
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    start_time = (bar - 1) * 1.5
    kick_start = start_time
    kick_end = kick_start + 0.375
    kick_3_start = start_time + 1.125
    kick_3_end = kick_3_start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_3_start, end=kick_3_end))

# Snare on 2 and 4
for bar in [2, 3, 4]:
    start_time = (bar - 1) * 1.5
    snare_start = start_time + 0.75
    snare_end = snare_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end))

# Hihat on every eighth
for bar in [2, 3, 4]:
    start_time = (bar - 1) * 1.5
    for i in range(8):
        hihat_start = start_time + i * 0.1875
        hihat_end = hihat_start + 0.1875
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
