
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# BAR 2 (1.5 - 3.0s)

# Marcus: Walking bass line in Fm (F, Ab, D, Eb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625), # D3
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # Eb3
]
bass.notes.extend(bass_notes)

# Diane: Open voicings (Fm7, Bbmaj7, Eb7, Abmaj7)
piano_notes = []
# Bar 2: Fm7 (F, Ab, C, Db)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # Db5
])
# Bar 3: Bbmaj7 (Bb, D, F, A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # A5
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # D5
])
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875))
    drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0))
    # Hi-hat on every eighth
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Dante: sax intro
# Bar 2: Start of motif (F4, G4, F4, Eb4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),  # F4
    pretty_midi.Note(velocity=110, pitch=66, start=1.6875, end=1.875), # G4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0625), # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.0625, end=2.25), # Eb4
]
# Bar 3: Leave it hanging (rest)
# Bar 4: Return and finish the motif (F4, G4, F4, Ab4)
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.6875),  # F4
    pretty_midi.Note(velocity=110, pitch=66, start=4.6875, end=4.875), # G4
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.0625), # F4
    pretty_midi.Note(velocity=110, pitch=62, start=5.0625, end=5.25), # Ab4
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
