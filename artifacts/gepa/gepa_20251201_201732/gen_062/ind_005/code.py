
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)
pm.time_signature_changes.append(time_signature)

# Define key signature
key_signature = pretty_midi.KeySignature(key_number=21, time=0.0)  # F minor
pm.key_signature_changes.append(key_signature)

# Define note durations (in seconds)
beat = 0.375  # 160 BPM, 4/4 time means each beat is 0.375s
bar = 4 * beat  # 1.5 seconds per bar

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass_instrument = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
piano_instrument = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums_instrument = pretty_midi.Instrument(program=drums_program)
pm.instruments.append(drums_instrument)

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax_instrument = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Bass line (walking line with chromatic approaches)
# Bar 1: D2 (38), F2 (41), G2 (43), F2 (41)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=beat),
    pretty_midi.Note(velocity=100, pitch=41, start=beat, end=2*beat),
    pretty_midi.Note(velocity=100, pitch=43, start=2*beat, end=3*beat),
    pretty_midi.Note(velocity=100, pitch=41, start=3*beat, end=bar),
]
bass_instrument.notes.extend(bass_notes)

# Bar 2: D2, F2, G2, C2 (chromatic approach to Bb)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=bar, end=bar + beat),
    pretty_midi.Note(velocity=100, pitch=41, start=bar + beat, end=bar + 2*beat),
    pretty_midi.Note(velocity=100, pitch=43, start=bar + 2*beat, end=bar + 3*beat),
    pretty_midi.Note(velocity=100, pitch=40, start=bar + 3*beat, end=bar * 2),
]
bass_instrument.notes.extend(bass_notes)

# Bar 3: D2, Bb2 (37), F2, G2
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=bar * 2, end=bar * 2 + beat),
    pretty_midi.Note(velocity=100, pitch=37, start=bar * 2 + beat, end=bar * 2 + 2*beat),
    pretty_midi.Note(velocity=100, pitch=41, start=bar * 2 + 2*beat, end=bar * 2 + 3*beat),
    pretty_midi.Note(velocity=100, pitch=43, start=bar * 2 + 3*beat, end=bar * 3),
]
bass_instrument.notes.extend(bass_notes)

# Bar 4: D2, F2, G2, D2 (resolution)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=bar * 3, end=bar * 3 + beat),
    pretty_midi.Note(velocity=100, pitch=41, start=bar * 3 + beat, end=bar * 3 + 2*beat),
    pretty_midi.Note(velocity=100, pitch=43, start=bar * 3 + 2*beat, end=bar * 3 + 3*beat),
    pretty_midi.Note(velocity=100, pitch=38, start=bar * 3 + 3*beat, end=bar * 4),
]
bass_instrument.notes.extend(bass_notes)

# Piano chords (open voicings, resolving on the last)
# Bar 1: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=0.0, end=beat),
    pretty_midi.Note(velocity=100, pitch=67, start=0.0, end=beat),
    pretty_midi.Note(velocity=100, pitch=69, start=0.0, end=beat),
    pretty_midi.Note(velocity=100, pitch=72, start=0.0, end=beat),
]
piano_instrument.notes.extend(piano_notes)

# Bar 2: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=bar, end=bar + beat),
    pretty_midi.Note(velocity=100, pitch=79, start=bar, end=bar + beat),
    pretty_midi.Note(velocity=100, pitch=77, start=bar, end=bar + beat),
    pretty_midi.Note(velocity=100, pitch=71, start=bar, end=bar + beat),
]
piano_instrument.notes.extend(piano_notes)

# Bar 3: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=bar * 2, end=bar * 2 + beat),
    pretty_midi.Note(velocity=100, pitch=68, start=bar * 2, end=bar * 2 + beat),
    pretty_midi.Note(velocity=100, pitch=71, start=bar * 2, end=bar * 2 + beat),
    pretty_midi.Note(velocity=100, pitch=70, start=bar * 2, end=bar * 2 + beat),
]
piano_instrument.notes.extend(piano_notes)

# Bar 4: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=bar * 3, end=bar * 4),
    pretty_midi.Note(velocity=100, pitch=67, start=bar * 3, end=bar * 4),
    pretty_midi.Note(velocity=100, pitch=69, start=bar * 3, end=bar * 4),
    pretty_midi.Note(velocity=100, pitch=72, start=bar * 3, end=bar * 4),
]
piano_instrument.notes.extend(piano_notes)

# Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
# Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + 0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.375 + 0.375),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.0 + 0.1875),  # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.1875 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.375 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.5625 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.75 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=0.9375 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.125 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.3125 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.5 + 0.1875),
]
drums_instrument.notes.extend(drum_notes)

# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=bar, end=bar + 0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=bar + 0.375, end=bar + 0.375 + 0.375),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=bar, end=bar + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar + 0.1875, end=bar + 0.1875 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar + 0.375, end=bar + 0.375 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar + 0.5625, end=bar + 0.5625 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar + 0.75, end=bar + 0.75 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar + 0.9375, end=bar + 0.9375 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar + 1.125, end=bar + 1.125 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar + 1.3125, end=bar + 1.3125 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar + 1.5, end=bar + 1.5 + 0.1875),
]
drums_instrument.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=bar * 2, end=bar * 2 + 0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=bar * 2 + 0.375, end=bar * 2 + 0.375 + 0.375),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 2, end=bar * 2 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 2 + 0.1875, end=bar * 2 + 0.1875 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 2 + 0.375, end=bar * 2 + 0.375 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 2 + 0.5625, end=bar * 2 + 0.5625 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 2 + 0.75, end=bar * 2 + 0.75 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 2 + 0.9375, end=bar * 2 + 0.9375 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 2 + 1.125, end=bar * 2 + 1.125 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 2 + 1.3125, end=bar * 2 + 1.3125 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 2 + 1.5, end=bar * 2 + 1.5 + 0.1875),
]
drums_instrument.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=bar * 3, end=bar * 3 + 0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=bar * 3 + 0.375, end=bar * 3 + 0.375 + 0.375),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 3, end=bar * 3 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 3 + 0.1875, end=bar * 3 + 0.1875 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 3 + 0.375, end=bar * 3 + 0.375 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 3 + 0.5625, end=bar * 3 + 0.5625 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 3 + 0.75, end=bar * 3 + 0.75 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 3 + 0.9375, end=bar * 3 + 0.9375 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 3 + 1.125, end=bar * 3 + 1.125 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 3 + 1.3125, end=bar * 3 + 1.3125 + 0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=bar * 3 + 1.5, end=bar * 3 + 1.5 + 0.1875),
]
drums_instrument.notes.extend(drum_notes)

# Saxophone motif - start on beat 1 of bar 2
# First note: A4 (69), start on beat 1 of bar 2 (bar * 1)
# Second note: D5 (72), start on beat 2 of bar 2 (bar * 1 + beat)
# Third note: F5 (74), start on beat 3 of bar 2 (bar * 1 + 2*beat)
# End on beat 4 with a rest

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=bar, end=bar + beat),
    pretty_midi.Note(velocity=100, pitch=72, start=bar + beat, end=bar + 2*beat),
    pretty_midi.Note(velocity=100, pitch=74, start=bar + 2*beat, end=bar + 3*beat),
]
sax_instrument.notes.extend(sax_notes)

# Write the MIDI file
pm.write("jazz_intro.mid")
