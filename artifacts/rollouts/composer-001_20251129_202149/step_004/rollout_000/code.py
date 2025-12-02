
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    time = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.375, end=time + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 1.125, end=time + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.1875)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # D#
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),  # G#
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25), # A#
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif, start it, leave it hanging, return to finish it
# C, E, Bb, F (C7 arpeggio)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # E
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.0625, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.6875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.0625, end=5.25), # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Full kit in bars 2-4
for bar in range(2, 4):
    time = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.375, end=time + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=time + 1.125, end=time + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + i * 0.375, end=time + i * 0.375 + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
