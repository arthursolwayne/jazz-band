
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
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5, note_number=42)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=3.0),  # D#
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625), # A#
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # B
]
piano.notes.extend(piano_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)

# Sax: short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25), # B
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
