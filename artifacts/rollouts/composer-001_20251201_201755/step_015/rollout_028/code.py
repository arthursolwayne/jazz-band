
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
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)      # Hihat on every eighth
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2 on 2
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # Eb2 on 3
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # A2 on 4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A (76)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # Bb (77)
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0)   # C (82)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Start motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # Bb (MIDI 67)
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25), # C (69)
    pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.625), # Bb (68)
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0)   # D (71)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (MIDI 43) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2 on 1
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # Bb2 on 2
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125), # A2 on 3
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),  # D2 on 4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),  # Bb (MIDI 77)
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5),  # D (82)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # F (71)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=4.5)   # Ab (79)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif, build tension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # D (MIDI 71)
    pretty_midi.Note(velocity=110, pitch=73, start=3.375, end=3.75), # E (73)
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125), # D (72)
    pretty_midi.Note(velocity=110, pitch=75, start=4.125, end=4.5)   # F (75)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: C2 (MIDI 48) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # C2 on 1
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # D2 on 2
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625), # C#2 on 3
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # E2 on 4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C (MIDI 72)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),  # E (77)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # G (79)
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=6.0)   # B (84)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif, resolve the tension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=75, start=4.5, end=4.875),  # F (MIDI 75)
    pretty_midi.Note(velocity=110, pitch=77, start=4.875, end=5.25), # G (77)
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.625), # F# (76)
    pretty_midi.Note(velocity=110, pitch=79, start=5.625, end=6.0)   # A (79)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)      # Hihat on every eighth
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
