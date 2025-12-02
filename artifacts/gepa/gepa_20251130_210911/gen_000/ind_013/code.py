
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in
# Sax: D (D4) to F# (F#4) to B (B4) to D (D5) - short motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=72, start=2.0625, end=2.25),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.6875),  # D3
    pretty_midi.Note(velocity=80, pitch=49, start=1.6875, end=1.875),  # Eb3
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0625),  # E3
    pretty_midi.Note(velocity=80, pitch=52, start=2.0625, end=2.25),  # F#3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on beat 2 (bar 2)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=2.0),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),  # B4
    pretty_midi.Note(velocity=85, pitch=64, start=1.875, end=2.0),  # F4
    # D7 on beat 4 (bar 2)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.4375),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.4375),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.4375),  # B4
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.4375),  # F4
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Sax continues motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=66, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=72, start=2.8125, end=3.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.4375),  # G3
    pretty_midi.Note(velocity=80, pitch=55, start=2.4375, end=2.625),  # A#3
    pretty_midi.Note(velocity=80, pitch=57, start=2.625, end=2.8125),  # C4
    pretty_midi.Note(velocity=80, pitch=59, start=2.8125, end=3.0),  # D#4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on beat 2 (bar 3)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.8125),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=2.8125),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=2.8125),  # B4
    pretty_midi.Note(velocity=85, pitch=64, start=2.625, end=2.8125),  # F4
    # D7 on beat 4 (bar 3)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.1875),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.1875),  # B4
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.1875),  # F4
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Sax finishes motif and hangs
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=72, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.1875),  # F#4
    pretty_midi.Note(velocity=80, pitch=62, start=3.1875, end=3.375),  # G#4
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5625),  # A#4
    pretty_midi.Note(velocity=80, pitch=66, start=3.5625, end=3.75),  # C#5
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.5),  # C#5 (hold)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on beat 2 (bar 4)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5625),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=3.375, end=3.5625),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5625),  # B4
    pretty_midi.Note(velocity=85, pitch=64, start=3.375, end=3.5625),  # F4
    # D7 on beat 4 (bar 4)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.9375),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=3.9375),  # A4
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=3.9375),  # B4
    pretty_midi.Note(velocity=85, pitch=64, start=3.75, end=3.9375),  # F4
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 and 4
for bar in [2, 3]:
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend([note for note in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
