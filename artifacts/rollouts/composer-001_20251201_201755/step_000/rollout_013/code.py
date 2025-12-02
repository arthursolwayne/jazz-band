
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # F#2 on 2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # A2 on 3
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # D2 on 4
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # E2 on 1
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # A2 on 2
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125), # F#2 on 3
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # D2 on 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # F#2 on 2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # A2 on 3
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # D2 on 4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25),  # C
]

# Bar 3: G7 (G B D F)
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),  # F
]

# Bar 4: A7 (A C# E G)
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.75),  # C#
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # G
]

# Bar 2-4: Comp on 2 and 4
# Bar 2: play on beat 2
for note in piano_notes:
    note.start += 0.75
    note.end += 0.75

# Bar 3: play on beat 2
for note in piano_notes:
    if note.start >= 2.25 and note.start < 3.0:
        note.start += 0.75
        note.end += 0.75

# Bar 4: play on beat 2
for note in piano_notes:
    if note.start >= 3.0 and note.start < 3.75:
        note.start += 0.75
        note.end += 0.75

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D D# E D (MIDI 62, 63, 64, 62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75), # D#
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875), # E
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D (hanging)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # D (return)
    pretty_midi.Note(velocity=100, pitch=63, start=2.375, end=2.5),  # D#
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # D
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
