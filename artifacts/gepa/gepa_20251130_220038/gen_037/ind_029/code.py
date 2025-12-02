
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
    # Hihat on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0), # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5), # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25), # G#
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0), # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25), # C#
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.75), # C#
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25), # C#
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante: Whisper to cry. One short motif, leave it hanging, return to finish it.
# Start with a whisper at the beginning of bar 2, then build
sax_notes = [
    # Bar 2: Whisper the motif
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.625), # F#
    pretty_midi.Note(velocity=80, pitch=69, start=1.625, end=1.75), # A
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875), # G
    # Bar 3: Let it breathe, then build
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.125), # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5), # F#
    # Bar 4: Finish the motif, cry out
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.625), # A
    pretty_midi.Note(velocity=110, pitch=71, start=4.625, end=4.75), # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=4.875), # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0), # G
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
