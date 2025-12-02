
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
bar_length = 1.5
for bar in range(1):
    start = bar * bar_length
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    kick_time = start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = start + 0.375
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    snare_time = start + 1.125
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat_time = start + i * 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - chromatic walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=63, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 0.75, end=1.5 + 1.125),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 1.125, end=1.5 + 1.5),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.5, end=1.5 + 1.875),
    pretty_midi.Note(velocity=100, pitch=68, start=1.5 + 1.875, end=1.5 + 2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 2.25, end=1.5 + 2.625),
    pretty_midi.Note(velocity=100, pitch=70, start=1.5 + 2.625, end=1.5 + 3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 3.0, end=1.5 + 3.375),
    pretty_midi.Note(velocity=100, pitch=73, start=1.5 + 3.375, end=1.5 + 3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5 + 3.75, end=1.5 + 4.125),
    pretty_midi.Note(velocity=100, pitch=75, start=1.5 + 4.125, end=1.5 + 4.5),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5 + 4.5, end=1.5 + 4.875),
    pretty_midi.Note(velocity=100, pitch=78, start=1.5 + 4.875, end=1.5 + 5.25),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5 + 5.25, end=1.5 + 5.625),
    pretty_midi.Note(velocity=100, pitch=80, start=1.5 + 5.625, end=1.5 + 6.0),
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.375, end=1.5 + 0.75),  # D7
    pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5 + 0.375, end=1.5 + 0.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.125, end=1.5 + 1.5),  # D7
    pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 1.125, end=1.5 + 1.5),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5 + 1.125, end=1.5 + 1.5),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5 + 1.125, end=1.5 + 1.5),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 2.625, end=1.5 + 3.0),  # D7
    pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 2.625, end=1.5 + 3.0),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5 + 2.625, end=1.5 + 3.0),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5 + 2.625, end=1.5 + 3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.375, end=1.5 + 3.75),  # D7
    pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 3.375, end=1.5 + 3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5 + 3.375, end=1.5 + 3.75),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5 + 3.375, end=1.5 + 3.75),
]
piano.notes.extend(piano_notes)

# Drums: continue from bar 1
for bar in range(2, 4):
    start = 1.5 + (bar - 1) * bar_length
    # Kick on 1 and 3
    kick_time = start + 0.0
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    kick_time = start + 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare_time = start + 0.375
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    snare_time = start + 1.125
    snare = pretty_midi.Note(velocity=110, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat_time = start + i * 0.375
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat)

# Sax (Dante) - motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.5 + 0.375),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.5 + 0.375, end=1.5 + 0.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=1.5 + 0.75, end=1.5 + 1.125),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=1.5 + 1.125, end=1.5 + 1.5),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=1.5 + 1.5, end=1.5 + 1.875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.5 + 1.875, end=1.5 + 2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=1.5 + 2.25, end=1.5 + 2.625),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=1.5 + 2.625, end=1.5 + 3.0),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=1.5 + 3.0, end=1.5 + 3.375),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.5 + 3.375, end=1.5 + 3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=1.5 + 3.75, end=1.5 + 4.125),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=1.5 + 4.125, end=1.5 + 4.5),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=1.5 + 4.5, end=1.5 + 4.875),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.5 + 4.875, end=1.5 + 5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=1.5 + 5.25, end=1.5 + 5.625),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=1.5 + 5.625, end=1.5 + 6.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
