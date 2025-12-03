
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
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
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # A2 on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C#5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - short motif, make it sing
# Start on D4 (62), move to F#4 (67), resolve on A4 (71)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4 on 1
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F#4 on 2
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # A4 on 3-4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # A2 on 1
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75), # Bb2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D2 on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: D7 (D-F#-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - echo the motif but with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4 on 1
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # F#4 on 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5),  # D4 on 3-4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Eb2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=45, start=5.625, end=6.0),  # A2 on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # C#5
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - finish the motif, leave a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4 on 1
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # F#4 on 2
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # A4 on 3
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # F#4 on 4 (hanging note)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
