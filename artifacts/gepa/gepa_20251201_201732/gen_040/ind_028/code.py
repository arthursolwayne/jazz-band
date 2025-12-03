
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
drum_notes = []
for i in range(4):  # 4 beats
    if i % 2 == 0:
        # Kick on 1 and 3
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=i * 0.375, end=i * 0.375 + 0.125))
    # Snare on 2 and 4
    if i % 2 == 1:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=i * 0.375, end=i * 0.375 + 0.125))
    # Hi-hat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i * 0.375, end=i * 0.375 + 0.125))
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (F2 - C3, MIDI 53 - 60)
# Roots: F2, Bb2, B2, Eb3
# Chromatic approaches: E2, Bb2, B2, D#3
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.625),  # F2
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.0),  # Bb2
    pretty_midi.Note(velocity=90, pitch=58, start=2.25, end=2.375), # B2
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=2.75)  # Eb3
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bbmaj7 (Bb, D, F, A)
# Bar 4: B7 (B, D#, F#, A)
piano_notes = [
    # Bar 2 (1.5 - 2.0)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.0),  # E5
    # Bar 3 (2.0 - 2.5)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5),  # F5
    pretty_midi.Note(velocity=100, pitch=77, start=2.0, end=2.5),  # A5
    # Bar 4 (2.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=73, start=2.5, end=3.0),  # D#5
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0),  # F#5
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=3.0),  # A5
]
piano.notes.extend(piano_notes)

# Drums continue from bar 1
drum_notes = []
for i in range(4):  # 4 beats
    if i % 2 == 0:
        # Kick on 1 and 3
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=(1.5 + i * 0.375), end=(1.5 + i * 0.375) + 0.125))
    # Snare on 2 and 4
    if i % 2 == 1:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=(1.5 + i * 0.375), end=(1.5 + i * 0.375) + 0.125))
    # Hi-hat on every eighth
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=(1.5 + i * 0.375), end=(1.5 + i * 0.375) + 0.125))
drums.notes.extend(drum_notes)

# Dante's sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Start on F4, Bb4, then a trill or lick, leave it hanging.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),  # F4
    pretty_midi.Note(velocity=110, pitch=74, start=1.625, end=1.75),  # Bb4
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.0),  # C5 (hangs)
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.375),  # F4
    pretty_midi.Note(velocity=110, pitch=73, start=2.375, end=2.5),  # Ab4
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=2.75),  # F4
    pretty_midi.Note(velocity=110, pitch=74, start=2.75, end=2.875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=76, start=2.875, end=3.0),  # C5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Write to MIDI file
# midi.write disabled
