
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum note numbers
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    # Time in seconds
    start_time = bar * 1.5
    # Kick on 1 and 3
    kick_time = start_time + 0.0
    kick2_time = start_time + 0.75
    # Snare on 2 and 4
    snare_time = start_time + 0.375
    snare2_time = start_time + 1.125
    # Hihat on every eighth
    hihat_times = [start_time + i * 0.375 for i in range(4)]

    for t in hihat_times:
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=t, end=t + 0.125)
        drums.notes.append(note)

    note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=kick, start=kick2_time, end=kick2_time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=snare, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=snare, start=snare2_time, end=snare2_time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Key: F minor (F, Ab, Bb)
# Scale degrees: F (1), Gb (2), Ab (3), A (4), Bb (5), B (6), C (7)

# Bass line: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    # Root F (F2, MIDI 53)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.5 + 0.375),
    # Chromatic approach to A (Ab, MIDI 50)
    pretty_midi.Note(velocity=60, pitch=50, start=1.5 + 0.375, end=1.5 + 0.75),
    # Root A (Ab, MIDI 50)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5 + 0.75, end=1.5 + 1.125),
    # Chromatic approach to C (B, MIDI 67)
    pretty_midi.Note(velocity=60, pitch=67, start=1.5 + 1.125, end=1.5 + 1.5),

    # Bar 3
    # Root C (C2, MIDI 60)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5 + 1.5, end=1.5 + 1.875),
    # Chromatic approach to Eb (D, MIDI 62)
    pretty_midi.Note(velocity=60, pitch=62, start=1.5 + 1.875, end=1.5 + 2.25),
    # Root Eb (Eb2, MIDI 62)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 2.25, end=1.5 + 2.625),
    # Chromatic approach to F (E, MIDI 64)
    pretty_midi.Note(velocity=60, pitch=64, start=1.5 + 2.625, end=1.5 + 3.0),

    # Bar 4
    # Root F (F2, MIDI 53)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5 + 3.0, end=1.5 + 3.375),
    # Chromatic approach to A (Ab, MIDI 50)
    pretty_midi.Note(velocity=60, pitch=50, start=1.5 + 3.375, end=1.5 + 3.75),
    # Root A (Ab, MIDI 50)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5 + 3.75, end=1.5 + 4.125),
    # Chromatic approach to C (B, MIDI 67)
    pretty_midi.Note(velocity=60, pitch=67, start=1.5 + 4.125, end=1.5 + 4.5)
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
fmin7 = [pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.375),  # F
         pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + 0.375),  # Ab
         pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.5 + 0.375),  # C
         pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.5 + 0.375)]  # Eb

# Bar 3: Bb7
bb7 = [pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.5, end=1.5 + 1.875),  # Bb
       pretty_midi.Note(velocity=90, pitch=76, start=1.5 + 1.5, end=1.5 + 1.875),  # D
       pretty_midi.Note(velocity=90, pitch=79, start=1.5 + 1.5, end=1.5 + 1.875),  # F
       pretty_midi.Note(velocity=80, pitch=84, start=1.5 + 1.5, end=1.5 + 1.875)]  # Ab

# Bar 4: Eb7
eb7 = [pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.0, end=1.5 + 3.375),  # Eb
       pretty_midi.Note(velocity=90, pitch=72, start=1.5 + 3.0, end=1.5 + 3.375),  # G
       pretty_midi.Note(velocity=90, pitch=76, start=1.5 + 3.0, end=1.5 + 3.375),  # Bb
       pretty_midi.Note(velocity=80, pitch=81, start=1.5 + 3.0, end=1.5 + 3.375)]  # Db

piano.notes.extend(fmin7)
piano.notes.extend(bb7)
piano.notes.extend(eb7)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (64), Ab (69), Gb (67), F (64)
# Bar 2: Start the motif
sax_note1 = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.25)
sax_note2 = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 0.25, end=1.5 + 0.5)
sax_note3 = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.5, end=1.5 + 0.75)
sax_note4 = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 0.75, end=1.5 + 1.0)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

# Bar 3: Leave it hanging (rest)
# No notes in bar 3

# Bar 4: Repeat the motif
sax_note5 = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 3.0, end=1.5 + 3.25)
sax_note6 = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 3.25, end=1.5 + 3.5)
sax_note7 = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.5, end=1.5 + 3.75)
sax_note8 = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 3.75, end=1.5 + 4.0)
sax.notes.extend([sax_note5, sax_note6, sax_note7, sax_note8])

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
