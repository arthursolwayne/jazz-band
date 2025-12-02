
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(0, 4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
    drums.notes.append(snare)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
# Dm7: D F A C
# Walking line: D F Eb G Ab Bb A C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D F A C
# Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=95, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),  # C
]
piano.notes.extend(piano_notes)

# Drums: continue same pattern
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(0, 4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
    drums.notes.append(snare)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm motif: D F A G (with a slight chromatic twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.5),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
