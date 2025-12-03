
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875), # F (D2)
    pretty_midi.Note(velocity=80, pitch=75, start=1.875, end=2.25), # C (G2)
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625), # Bb (F#2)
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0), # F (D2)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0), # F (E4)
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0), # A (G4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0), # C (F4)
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=3.0), # E (G#4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # G (F4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25), # C (F4)
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # G (F4)
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0), # C (F4)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=75, start=3.0, end=3.375), # C (G2)
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75), # Bb (F#2)
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.125), # F (D2)
    pretty_midi.Note(velocity=80, pitch=68, start=4.125, end=4.5), # Eb (C2)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Bb7 (Bb D F Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5), # Bb (F4)
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=4.5), # D (G#4)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=4.5), # F (E4)
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=4.5), # Ab (F#4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # C (F4)
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # G (F4)
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # C (F4)
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5), # G (F4)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875), # Eb (C2)
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.25), # F (D2)
    pretty_midi.Note(velocity=80, pitch=75, start=5.25, end=5.625), # C (G2)
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=6.0), # Bb (F#2)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0), # C (F4)
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=6.0), # Eb (F#4)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0), # G (E4)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0), # Bb (F4)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # G (F4)
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25), # C (F4)
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # G (F4)
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0), # C (F4)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('wayne_intro.mid')
