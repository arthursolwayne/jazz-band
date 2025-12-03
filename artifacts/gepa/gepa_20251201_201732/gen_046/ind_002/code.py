
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F, Ab, G, Eb), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),   # F2 (root)
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.625),  # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),   # Eb2 (fifth of Ab)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=3.0),  # D5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.875),  # F4 (return)
    pretty_midi.Note(velocity=100, pitch=68, start=2.875, end=3.0),   # Ab4 (finish)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm (F, Ab, G, Eb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),   # F2
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),  # G2
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125),  # Gb2
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),   # Eb2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # Eb5
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),  # G5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # Eb4
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # F#4 (tension)
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),   # Eb4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm (F, Ab, G, Eb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),   # F2
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625),  # Gb2
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),   # Eb2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C5
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=6.0),  # D5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish motif, resolve on D (tension to resolution)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # Eb4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=100, pitch=73, start=5.625, end=6.0),   # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
