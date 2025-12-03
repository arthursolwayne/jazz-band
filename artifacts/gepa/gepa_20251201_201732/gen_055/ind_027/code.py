
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full band enters
# Bass: root and fifth with chromatic approach
# D2 (D) and A2 (A) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # A2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: D7sus4 (D, G, A, C#) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=2.0),  # F#4 (C#)
]

# Bar 3: G7 (G, B, D, F#)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=80, pitch=76, start=2.0, end=2.5),  # F#5
])

# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=3.0),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=3.0),  # B4
])

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, concise, melodic, memorable
# D4 (D), F#4 (F#), A4 (A), D5 (D) - with syncopation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.375),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=2.375, end=2.75),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=2.75, end=3.0),   # D5
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0]:
    # Bar 2 and 3
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
        pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75),
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125),
        pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5),
        pretty_midi.Note(velocity=60, pitch=42, start=bar_start, end=bar_start + 1.5)
    ]
    for note in drum_notes:
        drums.notes.append(note)

# Bar 4: Same rhythm
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=4.5)
]
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to MIDI file
# midi.write disabled
