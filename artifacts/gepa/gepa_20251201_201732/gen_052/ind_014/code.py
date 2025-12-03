
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Marcus: Walking bass line in F (F2 - C3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # D2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # F2
]

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25),  # E
]

# Bar 3 (3.0 - 4.5s)
# Diane: Bb7 (Bb, D, F, Ab)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # Ab
]

# Bar 4 (4.5 - 6.0s)
# Diane: Dm7 (D, F, A, C)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # C
]

# Add piano notes
for note in piano_notes:
    piano.notes.append(note)

# Add bass notes
for note in bass_notes:
    bass.notes.append(note)

# Dante: Sax solo, 4-bar motif in F, one phrase, open-ended
# F - G - Bb - F (motif), start at 1.5s, end at 3.0s, then rest until 6.0s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
