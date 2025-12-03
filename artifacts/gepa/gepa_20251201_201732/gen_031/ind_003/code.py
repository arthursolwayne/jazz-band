
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
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb) open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - one short motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),  # Db
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbm7 (Bb, Db, F, Ab) open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5),  # Db
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif with tension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # Db
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fm7 again, but with tension
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),  # Ab
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif with a return to A, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for Bar 3-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3, 6):
    start_time = bar * 1.5
    kick_start = start_time
    kick_end = start_time + 0.375
    snare_start = start_time + 0.75
    snare_end = start_time + 1.125
    hihat_start = start_time
    hihat_end = start_time + 1.5
    # Kick
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 1.125, end=kick_end + 1.125))
    # Snare
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start + 1.125, end=snare_end + 1.125))
    # Hihat
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
