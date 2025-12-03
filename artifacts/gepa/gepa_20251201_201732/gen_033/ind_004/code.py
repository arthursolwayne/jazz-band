
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
# Fm7: F, Ab, C, Db
# Walking line: F -> Eb -> D -> C -> Bb -> A -> Ab -> G -> F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm (F, Ab, C, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0),  # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches (Am7)
# A, C, E, F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # G#
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=100, pitch=61, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Am7 (A, C, E, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=4.5),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - continuation of motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches (Dm7)
# D, F, A, Bb
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),  # C#
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=100, pitch=58, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=5.75, end=6.0),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 (D, F, A, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - finish the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start+0.375)  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=start+0.75, end=start+1.125)  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start+1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=start+0.375, end=start+1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=start+0.75, end=start+1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=start+1.125, end=start+1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=start+1.125, end=start+1.5)  # Kick on 3

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
