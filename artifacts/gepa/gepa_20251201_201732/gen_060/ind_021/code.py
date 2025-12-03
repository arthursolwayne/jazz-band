
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
    
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in. Sax starts the melody
# F7 - E7 - D7 - F7 (short motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.6875),  # F7
    pretty_midi.Note(velocity=100, pitch=86, start=1.6875, end=1.875), # E7
    pretty_midi.Note(velocity=100, pitch=84, start=1.875, end=2.0),   # D7
    pretty_midi.Note(velocity=100, pitch=87, start=2.0, end=2.1875)  # F7
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F (D2 - G2 - A2 - C3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0)  # C3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875)  # E
]

# Bar 3: Dm7 (D, F, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=58, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625)  # C
])

# Bar 4: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=3.0), # B
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0)  # F
])

for note in piano_notes:
    piano.notes.append(note)

# Drums continue for bars 2-4
# Kick on 1 and 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)
])

# Snare on 2 and 4
drum_notes.extend([
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125)
])

# Hihat on every eighth
for start in [1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 3.0, 3.1875, 3.375, 3.5625]:
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
