
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (MIDI 53) to C3 (MIDI 58), walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F2 on 1
    pretty_midi.Note(velocity=100, pitch=51, start=1.75, end=2.0),  # Eb2 chromatic approach on 2
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.25),  # C3 on 3
    pretty_midi.Note(velocity=100, pitch=56, start=2.25, end=2.5),  # Bb2 chromatic approach on 4
]

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # Ab (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # Eb (MIDI 69)
]

# Sax: Motif (F, Ab, C, F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # F
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 to Bb2 (MIDI 53 to 56), walking line with chromatic approaches
bass_notes += [
    pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=3.25),  # Bb2 on 1
    pretty_midi.Note(velocity=100, pitch=54, start=3.25, end=3.5),  # A2 chromatic approach on 2
    pretty_midi.Note(velocity=100, pitch=58, start=3.5, end=3.75),  # C3 on 3
    pretty_midi.Note(velocity=100, pitch=56, start=3.75, end=4.0),  # Bb2 on 4
]

# Piano: Ab7 (Ab, C, Eb, Gb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # Ab (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # C (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # Eb (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=4.5),  # Gb (MIDI 63)
]

# Sax: Repeat motif with slight variation (F, Ab, C, F)
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # F
]

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 to C3 (MIDI 53 to 58), walking line with chromatic approaches
bass_notes += [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75),  # F2 on 1
    pretty_midi.Note(velocity=100, pitch=51, start=4.75, end=5.0),  # Eb2 chromatic approach on 2
    pretty_midi.Note(velocity=100, pitch=58, start=5.0, end=5.25),  # C3 on 3
    pretty_midi.Note(velocity=100, pitch=56, start=5.25, end=5.5),  # Bb2 chromatic approach on 4
]

# Piano: Fm7 (F, Ab, C, Eb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # Ab (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # C (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # Eb (MIDI 69)
]

# Sax: End motif (F, Ab, C, F) with a slight hold on F
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=6.0),  # F (held)
]

# Add notes to instruments
for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

# Bar 1: Drums only
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
# midi.write disabled
